var viewer;

function openOpenSeaDragon(fileInput) {
    const loader = document.getElementById('loader_box');
    loader.style.display = 'none';

    const shower = document.getElementById('openSeaDragon-window');
    shower.style.display = 'block';

    const file = fileInput.files[0];
    const image = URL.createObjectURL(file);
    viewer = OpenSeadragon({
        id: "openSeaDragon-window",
        prefixUrl: "../static/openseadragon/images/",
        tileSources: {
            type: 'image',
            url: image,
        },
    });

}

function onLoad() {
            //TODO:add openOpenSeaDragon(image of the page)
        }

        window.onload = onLoad();