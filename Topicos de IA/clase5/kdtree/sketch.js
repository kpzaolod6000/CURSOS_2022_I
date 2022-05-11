function setup () {
    let width = 250;
    let height = 200;
    
    createCanvas (width , height ) ;
    background (0) ;
    
    for (var x = 0; x < width ; x += width / 10) {
        
        for (var y = 0; y < height ; y += height / 5) {
            stroke (125 , 125 , 125) ;
            strokeWeight (0.3) ;
            line (x, 0, x, height );
            line (0 , y, width , y);
        }
    }
    
    // var data = [];
    // for ( let i = 0; i < 6; i ++) {
    //     var x = Math . floor ( Math . random () * height );
    //     var y = Math . floor ( Math . random () * height );
    //     data . push ([x, y]) ;
    //     fill (255 , 255 , 255) ;
    //     circle (x, height - y, 7) ; // 200 -y para q se dibuje apropiadamente
    //     textSize (8) ;
    //     text (x + ',' + y, x + 5, height - y);// 200 -y para q se dibuje apropiadamente
    // }

  
    let data = [[40 ,70],
                [70 ,130],
                [90 ,40],
                [110 , 100],
                [140 ,110],
                [160 , 100]];
    for ( let i = 0; i < data.length; i ++) {
        let x = data[i][0]
        let y = data[i][1]
        fill (255 , 255 , 255) ;
        circle (x, height - y, 7) ; // 200 -y para q se dibuje apropiadamente
        textSize (8) ;
        text (x + ',' + y, x + 5, height - y);// 200 -y para q se dibuje apropiadamente
    }
    console.log(data);
    let root = build_kdtree(data);
    console.log(root);
    console.log("Altura del arbol es: " + getHeight(root))

    // Para generar graficos

	
	let dotString = generate_dot(root);
	console.log(dotString);
    let graph = d3.select("#graph");
    graph.graphviz().renderDot(dotString);

    graficar(root,width,height);
        
    //querie

    let pQuery = [120 ,90]
    fill (255 , 125 , 125) ;
    circle (pQuery[0], height - pQuery[1], 7) ;
    textSize (8) ;
    text (pQuery[0] + ',' + pQuery[1], pQuery[0] + 5, height - pQuery[1]);

   console.log(closest_point_brute_force(data,pQuery));
   console.log(naive_closest_point(root,pQuery));
}
