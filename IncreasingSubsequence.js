function lisEndingAtIdx(arr, idx) {

    if (idx === 0)
        return 1;

    let mx = 1;
    for (let prev = 0; prev < idx; prev++) {
        // console.log("ini idx" + idx)
        if (arr[prev] < arr[idx]) {
            mx = Math.max(mx, lisEndingAtIdx(arr, prev) + 1);
        }
    }
    return mx;
}

function lis(arr) {
    let n = arr.length;
    console.log("ini lenght " + n)
    let largest = 1;
    for (let idx = 1; idx < n; idx++) {
        largest = Math.max(largest, lisEndingAtIdx(arr, idx)); // 2
        // console.log("ini nge cek dari " + arr[idx])
    }
    return largest;
}

// urutan bilangan yang diminta : 4, 1, 13, 7, 0, 2, 8, 11, 3
// let arr = [4, 1, 13, 7, 0, 2, 8, 11, 3];
// let arr = [1,2,3];
let arr = [2,4,1,13];
console.log(lis(arr));