var s,
	g = {
		nodes: [],
		edges: []
	};


// Instantiate sigma:
s = new sigma({
	graph: g,
	renderer: {
		container: "black-body",
		type: 'canvas'
	}
});

//load neo4j
sigma.neo4j.cypher(
	{ url: 'http://localhost:7474', user: 'neo4j', password: 'neo4j' },
	'match (p:Person {fullNameInChinese: \'郭台銘\'}) return p',
	s,
	function(s) {
		console.log('Number of nodes :'+ s.graph.nodes().length);
		console.log('Number of edges :'+ s.graph.edges().length);
		initData(s);
		s.refresh();
	}
);

//enable drag
dragListener = sigma.plugins.dragNodes(s, s.renderers[0]);
dragListener.bind('startdrag', function (event) {
});
dragListener.bind('drag', function (event) {
});
dragListener.bind('drop', function (event) {
});
dragListener.bind('dragend', function (event) {
});

function initData(s){
	s.graph.nodes().forEach(function (n) {
		switch (n.neo4j_labels[0]) {
			case "Company":
				n.label = n.neo4j_data.name;
				n.type = "star";
				break;
			case "Person":
				if(n.neo4j_data.fullNameInChinese != null){
					n.label = n.neo4j_data.fullNameInChinese
				}
				else{
					n.label = n.neo4j_data.fullName;
				}
				break;
		}
		if (n.neo4j_data.sanctionedEntity ==="true") {
			node.color = "red"
		}
	});
	s.graph.edges().forEach(function (e) {
		console.log(e);
		console.log(e.type);
		console.log(e.color);
	})
}

//tooltip
var config = {
	node: [{
	// 	show: 'hovers',
	// 	hide: 'hovers',
	// 	cssClass: 'sigma-tooltip',
	// 	position: 'top',
	// 	//autoadjust: true,
	// 	template:
	// 	'<div class="arrow"></div>' +
	// 	' <div class="sigma-tooltip-header">{{label}}</div>' +
	// 	'  <div class="sigma-tooltip-body"> ' +
	// 	'    <table>' +
	// 	'    </table>' +
	// 	'  </div>' +
	// 	'  <div class="sigma-tooltip-footer">Number of connections: {{degree}}</div>',
	// 	renderer: function(node, template) {
	// 		// The function context is s.graph
	// 		node.degree = this.degree(node.id);
	// 		// Returns an HTML string:
	// 		return Mustache.render(template, node);
	// 		// Returns a DOM Element:
	// 		//var el = document.createElement('div');
	// 		//return el.innerHTML = Mustache.render(template, node);
	// 	}
	//},{
		show: 'rightClickNode',
		cssClass: 'sigma-tooltip',
		position: 'right',
		template:
		'<div class="arrow"></div>' +
		' <div class="sigma-tooltip-header">{{label}}</div>' +
		'  <div class="sigma-tooltip-body">' +
		' <content></content>' +
		'  </div>' +
		' <div class="sigma-tooltip-footer">Number of connections: {{degree}}</div>',
		renderer: function (node, template) {
			var content = "";
			content += "<div><a href='#' DEFAULT' data-value='" + node.id +"' onclick='rightClickExpand(this)'>Expand All Relation</a></div>";
			template = template.replace('<content></content>', content);
			node.degree = this.degree(node.id);
			return Mustache.render(template, node);
		}
	}],
	stage: {
		template:
		'<div class="arrow"></div>' +
		'<div class="sigma-tooltip-header"> Menu </div>'
	}
};
// Instanciate the tooltips plugin with a Mustache renderer for node tooltips:
var tooltips = sigma.plugins.tooltips(s, s.renderers[0], config);
