k = 2;


class Node {

constructor (point , axis ){
    this.point = point ;
    this.left = null ;
    this.right = null ;
    this.axis = axis ;
    }
}

function getHeight ( node ) {}
function generate_dot ( node ) {}


function build_kdtree( points , depth = 0) {

    if (points.length == 0) return null;
    
    n = points.length
    m = points[0].length
    // console.log(n)
    // console.log(m)
    
    axis = depth % m;

    points.sort((a,b) => a[axis] - b[axis]);
      
    console.log(points)
    console.log(axis)

    ind = Math.floor(n/2)
    median = points[ind]
    console.log(median);

    node = new Node(median,axis)
    
    node.left = build_kdtree(points.slice(0,ind),depth+1)
    node.right = build_kdtree(points.slice(ind+1,depth+1))

    return node;


}

points = [[40 ,70],
[70 ,130],
[90 ,40],
[110 , 100],
[140 ,110],
[160 , 100]]
console.log(points)
root = build_kdtree(points)
console.log(root)



