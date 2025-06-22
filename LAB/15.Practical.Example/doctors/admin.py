from django.contrib import admin
from django.utils.html import format_html
from .models import Doctor, Specialization

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor_count')
    search_fields = ('name', 'description')
    
    def doctor_count(self, obj):
        return obj.doctor_set.count()
    doctor_count.short_description = 'Number of Doctors'

class DoctorAdmin(admin.ModelAdmin):
    # Display options
    list_display = (
        'profile_thumbnail',
        'full_name',
        'specialization',
        'age',
        'years_of_experience',
        'contact_info',
        'availability_status',
        'is_active',
    )
    
    list_display_links = ('full_name',)
    list_filter = (
        'specialization',
        'gender',
        'availability',
        'is_active',
        'joined_date',
    )
    search_fields = (
        'first_name',
        'last_name',
        'license_number',
        'email',
        'contact_number',
    )
    list_per_page = 25
    date_hierarchy = 'joined_date'
    ordering = ('last_name', 'first_name')
    readonly_fields = ('age', 'joined_date', 'last_updated')
    fieldsets = (
        ('Personal Information', {
            'fields': (
                ('first_name', 'last_name'),
                'gender',
                'date_of_birth',
                'age',
                'profile_picture',
            )
        }),
        ('Professional Information', {
            'fields': (
                'specialization',
                'license_number',
                'years_of_experience',
            )
        }),
        ('Contact Information', {
            'fields': (
                'contact_number',
                'email',
                'address',
            )
        }),
        ('Status', {
            'fields': (
                'availability',
                'is_active',
            )
        }),
        ('Metadata', {
            'fields': (
                'joined_date',
                'last_updated',
                'notes',
            ),
            'classes': ('collapse',),
        }),
    )
    
    # Custom methods for list display
    def full_name(self, obj):
        return f"{obj.last_name}, {obj.first_name}"
    full_name.short_description = 'Name'
    full_name.admin_order_field = 'last_name'
    
    def profile_thumbnail(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;" />',
                obj.profile_picture.url
            )
        return "-"
    profile_thumbnail.short_description = 'Photo'
    
    def contact_info(self, obj):
        return format_html(
            '<strong>Phone:</strong> {}<br><strong>Email:</strong> {}',
            obj.contact_number,
            obj.email
        )
    contact_info.short_description = 'Contact'
    
    def availability_status(self, obj):
        status_map = {
            'A': ('success', 'Available'),
            'B': ('warning', 'On Break'),
            'L': ('info', 'On Leave'),
            'U': ('danger', 'Unavailable'),
        }
        color, text = status_map.get(obj.availability, ('secondary', 'Unknown'))
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            color, text
        )
    availability_status.short_description = 'Status'
    
    # Custom actions
    actions = ['make_available', 'make_unavailable']
    
    def make_available(self, request, queryset):
        updated = queryset.update(availability='A')
        self.message_user(request, f"{updated} doctors marked as available.")
    make_available.short_description = "Mark selected doctors as available"
    
    def make_unavailable(self, request, queryset):
        updated = queryset.update(availability='U')
        self.message_user(request, f"{updated} doctors marked as unavailable.")
    make_unavailable.short_description = "Mark selected doctors as unavailable"
    
    # Custom change list view
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['specializations'] = Specialization.objects.all()
        return super().changelist_view(request, extra_context=extra_context)
    
    # Custom change form view
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        return super().changeform_view(request, object_id, form_url, extra_context)

# Register models
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Doctor, DoctorAdmin)

# Admin site customization
admin.site.site_header = "Doctor Management System"
admin.site.site_title = "Doctor Admin Portal"
admin.site.index_title = "Welcome to Doctor Management"