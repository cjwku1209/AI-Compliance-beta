function draw() {
	var config = {
		container_id: "black-body",
		server_url: "bolt://localhost:7687",
		server_user: "neo4j",
		server_password: "neo4j",
		labels: {
			"Company": {
				caption: "name",
				color: "red"
			}
		},
		relationships: {

		},
		initial_cypher: "MATCH (a:Person {fullName: \"Anna Murdoch Mann\"}) MATCH (b:Person {fullName: \"Paul Cheesbrough\"}) MATCH p=ShortestPath((a)-[*..4]-(b)) RETURN p"
	}
	var viz = new NeoVis.default(config);
	viz.render();
}

$("#search").on('click', function () {
	draw()
});