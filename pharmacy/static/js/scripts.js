// Import Bootstrap's CSS
import 'bootstrap/dist/css/bootstrap.min.css';

// Import Bootstrap's JavaScript (including its dependencies like Popper.js)
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import 'datatables.net';
import toastr from 'toastr';
import Swal from 'static/js/sweetalert2';
import $ from 'jquery';


window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

// Utility functions for alerts

// ✅ Toastr Notification Function
function showToastr(type, message) {
    toastr.options = {
        "closeButton": true,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "timeOut": "3000"
    };

    if (type === "success") {
        toastr.success(message);
    } else if (type === "error") {
        toastr.error(message);
    } else if (type === "warning") {
        toastr.warning(message);
    } else {
        toastr.info(message);
    }
}

// ✅ SweetAlert Confirmation Dialog
function showConfirmationDialog(title, text, confirmCallback) {
    Swal.fire({
        title: title,
        text: text,
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, confirm!"
    }).then((result) => {
        if (result.isConfirmed) {
            confirmCallback(); // Execute callback function
        }
    });
}

