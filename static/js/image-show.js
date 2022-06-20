var viewer;

function onLoad() {
    viewer = OpenSeadragon({
        id: "openSeaDragon-window",
        prefixUrl: "../static/openseadragon/images/",
        tileSources: "../static/img/example.dzi"
    });
}

window.onload = onLoad();