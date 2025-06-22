$(document).ready(function() {
    // Create doctor modal
    $(".js-create-doctor").click(function() {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $("#modal-doctor").modal("show");
            },
            success: function(data) {
                $("#modal-doctor .modal-content").html(data.html_form);
            }
        });
    });

    // Update doctor modal
    $("#doctor-table").on("click", ".js-update-doctor", function() {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $("#modal-doctor").modal("show");
            },
            success: function(data) {
                $("#modal-doctor .modal-content").html(data.html_form);
            }
        });
    });

    // Delete doctor modal
    $("#doctor-table").on("click", ".js-delete-doctor", function() {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $("#modal-doctor").modal("show");
            },
            success: function(data) {
                $("#modal-doctor .modal-content").html(data.html_form);
            }
        });
    });

    // Save form (create/update)
    $("#modal-doctor").on("submit", ".js-doctor-create-form, .js-doctor-update-form", function() {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    $("#doctor-table").html(data.html_doctor_list);
                    $("#modal-doctor").modal("hide");
                } else {
                    $("#modal-doctor .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

    // Delete form
    $("#modal-doctor").on("submit", ".js-doctor-delete-form", function() {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    $("#doctor-table").html(data.html_doctor_list);
                    $("#modal-doctor").modal("hide");
                }
            }
        });
        return false;
    });
});