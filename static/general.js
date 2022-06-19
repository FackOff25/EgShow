var viewer;

function openOpenSeaDragon(fileInput) {
	var loader = document.getElementById('loader_box');
	loader.style.display = 'none';

	var shower = document.getElementById('openseadragon1');
	shower.style.display = 'block';
	
	const file = fileInput.files[0];
	var image = URL.createObjectURL(file);	
	viewer = OpenSeadragon({
		id: "openseadragon1",
		prefixUrl: "static/openseadragon/images/",
		tileSources:   {
			type: 'image',
			url:  image,
		},
	});

  }