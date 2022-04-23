img = [3, 4, 2, 3, 0, -3, 9, 11, 23, 12, 23, 2, 13, 4, 56, 3, 5, 9, 3, 5, 5, 1, 4, 9]; //2x4x3



let gris = []
let parameter = [0.299,0.587,0.114] //red,green,blue

for (let i = 0; i < img.length-2; i+=3) {
    sum = 0;
    indx = 0;
    for(let j=i;j<i+3;j++){
        sum += img[j]*parameter[indx++];
    }
    gris.push(sum);
}

console.log(gris);
console.log(gris.length);