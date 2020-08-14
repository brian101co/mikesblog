document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.sidenav');
    let instances = M.Sidenav.init(elems);

    let images = document.querySelectorAll('.materialboxed');
    let image_instances = M.Materialbox.init(images);
});