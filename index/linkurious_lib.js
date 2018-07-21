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
	'match (p:Person {fullName: \'James Rupert Murdoch\'}) -[:SPOUSE|CHILDREN] -(s:Person)  return p, s',
	s,
	function(s) {
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
		console.log(n);
		n.label = n.neo4j_data.fullName;
		console.log(n.neo4j_data.fullName);
		Define_Node_Edge_Color_Shape(s)
	});
}

/* ##### HP May 03 2018.  Define a function for the color and shape of nodes and edges.  */
function Define_Node_Edge_Color_Shape(s) {

	var nodes_list = s.graph.nodes();
	var edege_list = s.graph.edges();

	g.nodes = nodes_list;
	g.edges = edege_list;

	for (i = 0; i < nodes_list.length; i++) {
		var node = nodes_list[i];


		if (node.neo4j_data.class_name === "Person") {
			if (node.neo4j_data.PEP === "True") {
				node.type = "pacman";
			} else node.type = "circle";
		}

		if (node.neo4j_data.sanctionedEntity ==="true") {
			node.color = "red"
		}
	}

}
