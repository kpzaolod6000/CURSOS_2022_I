k = 2;



class Node {

constructor (point , axis ){
    this.point = point;
    this.left = null;
    this.right = null;
    this.axis = axis;
    }
}

function getHeight ( node ) {
	if (!node) return -1;
	else return 1 + Math.max(getHeight(node.left), getHeight(node.right));
}


function graficar(node,width,height,nFather=null){
	if (!node) return ;
	else {
		let pnt =  node.point
		if (nFather){
			if (node.axis == 0){
			
				stroke (125 , 125 , 225) ;
				strokeWeight (0.8) ;
				if (pnt[1] > nFather.point[1]) {
					line (pnt[0], 0, pnt[0],  height - nFather.point[1]);	
				}else{
					line (pnt[0], height, pnt[0],height-nFather.point[1]);	
				}
				
			}else if (node.axis == 1) {
				stroke (125 , 125 , 225) ;
				strokeWeight (0.8) ;
				if (pnt[0] > nFather.point[0]) {
					line (nFather.point[0] , height - pnt[1], width ,height-pnt[1]);		
				}else{
					line (0, height - pnt[1],nFather.point[0],height-pnt[1]);		
				}
				
			}
		}else {
			stroke (125 , 125 , 225) ;
			strokeWeight (0.8) ;
			line (pnt[0], 0, pnt[0], height );
		}
		graficar(node.left,width,height,node);
		graficar(node.right,width,height,node);		
	}
}

function build_kdtree( points , depth = 0) {

    if (points.length == 0) return null;
    
    let n = points.length;
    let m = points[0].length;
    // console.log(n)
    // console.log(m)
    
    let axis = depth % m;

    points.sort((a,b) => a[axis] - b[axis]);
      
    console.log(points);
    console.log(axis);

    let ind = Math.floor(n/2);
    let median = points[ind];
    console.log(median);

    let node = new Node(median,axis);
    
    node.left = build_kdtree(points.slice(0,ind),depth+1);
    node.right = build_kdtree(points.slice(ind+1,n),depth+1);

    return node;
}

function generate_dot(node) {
	let string = "digraph G {\n";
 	string = string + recursive_generate_dot(node);
	string = string + "}\n";
	return string;
}

function recursive_generate_dot(node) {
	let txt = "";
	if (node) {
		if (node.left) {
			txt = txt + '\t"';
			txt = txt + node.point;
			txt = txt + '" -> "';
			txt = txt + node.left.point;
			txt = txt + '";\n';
			txt = txt + recursive_generate_dot(node.left);
		}
		if (node.right) {
			txt = txt + '\t"';
			txt = txt + node.point;
			txt = txt + '" -> "';
			txt = txt + node.right.point;
			txt = txt + '";\n';
			txt = txt + recursive_generate_dot(node.right);
		}
	}
	return txt;
}

function distanceSquared(point1, point2) {
	var distance = 0;
	for (var i = 0; i < k; i++) distance += Math.pow(point1[i] - point2[i], 2);
	return Math.sqrt(distance);
}


function closest_point_brute_force(points, point) {
	if (points.length < 1) return null;
	if (points.length == 1) return points[0];

	var min = distanceSquared(point, points[0]);
	var minPoint = points[0];

	for (let i = 1; i < points.length; i++) {
		var distance = distanceSquared(point, points[i]);
		if (distance < min) {
			min = distance;
			minPoint = points[i];
		}
	}

	return minPoint;
}


function naive_closest_point(node, point, depth = 0, best = null) {
	if (!node) return best;

	if (!depth) {
		best = node.point;
	} else {
		if (distanceSquared(node.point, point) < distanceSquared(best, point)) {
			best = node.point;
		}
	}

	var axis = depth % node.point.length;

	if (point[axis] < node.point[axis]) {
		return naive_closest_point(node.left, point, depth + 1, best);
	} else {
		return naive_closest_point(node.right, point, depth + 1, best);
	}
}

function closest_point(node, point, depth = 0, best = null) {
	if (!node) return best;

	if (!depth) {
		best = node.point;
	} else {
		if (distanceSquared(node.point, point) < distanceSquared(best, point)) {
			best = node.point;
		}
	}
	var axis = depth % node.point.length;

	if (point[axis] < node.point[axis]) {
		best = closest_point(node.left, point, depth + 1, best);
		if (
			Math.abs(point[axis] - node.point[axis]) <
			distanceSquared(point, best)
		)
			best = closest_point(node.right, point, depth + 1, best);
	} else {
		best = closest_point(node.right, point, depth + 1, best);
		if (
			Math.abs(point[axis] - node.point[axis]) <
			distanceSquared(point, best)
		)
			best = closest_point(node.left, point, depth + 1, best);
	}
	return best;
}