text1 = 'aaaa'
text2 = 'aaa'

n_t1 = text1.length
n_t2 = text2.length

min_t = Math.min(n_t1,n_t2)

grad = min_t //100%
for (i=0; i<min_t;i++){
    if (text1[i] !== text2[i]) {
        grad--
    }
}
if (n_t1 === n_t2 ) {
    console.log((grad/min_t*100).toFixed(2)+ '%')
}
else{
        
    diff = Math.abs(n_t1 - n_t2)
    grad = grad - diff
    console.log((grad/min_t*100).toFixed(2)+ '%')
}