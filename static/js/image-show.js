
function onLoad() {
    const shower = document.getElementById('openSeaDragon-window');
    const image = shower.dataset.image

    /*let viewer = */OpenSeadragon({
        id: "openSeaDragon-window",
        prefixUrl: "../static/openseadragon/images/",
        tileSources: image
    });
}

window.onload = onLoad();