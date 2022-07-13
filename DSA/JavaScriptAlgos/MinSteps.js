// def arrChallange(arr):
// swap_count = 0
// dict_arr = {k: v for v, k in enumerate(arr)}

// # sort this dictionary

// sorted_dict = dict(sorted(dict_arr.items()))
// for i in range(len(arr)):
//     if(i==list(sorted_dict.values())[i]):
//         continue
//     else:
//         swap_count+=1
//         print('unequal')

// Sort the unsorted arra then convert it back to unsorted one to get min swaps

// ### [1,3,4,2]

// #### {(1,0),(3,1),(4,2),(2,3)}  Before sortng

// ### Sort by key

// ### {(1,0),(2,3),(3,1),(4,2)}  ====> iterate

// ### loop trought this dict
// ### for i in range dict:
// ### if value_index == i
//     ### continue

// ### swap_count ++
// ### i=1
// ### value_index=3
// ### swap(i,value_index)
// ### i -- to check weather swapeed value is i place or not

// 2 arr 1 for elem and one to store its index
// sort the temp arr

// const arrChallange = (arr) => {
//   let n = arr.length;
//   let tempArr = [];
//   let swapCount = 0;

//   for (let i = 0; i < n; i++) {
//     tempArr.push([arr[i], i]);
//   }
//   sorted_arr = tempArr.sort();

//   //   to keep track of visited elem
//   let visitedElem = new Array(n);

//   for (let i = 0; i < n; i++) {
//     visitedElem[i] = false;
//   }
// };

const swap = (arr, i, j) => {
  [arr[i], arr[j]] = [arr[j], arr[i]];
};

const arrChallange = (arr) => {
  let swapCount = 0;
  let tempArr = [...arr];
  tempArr.sort();

  for (let i = 0; i < tempArr.length; i++) {
    if (arr[i] == tempArr[i]) {
      continue;
    } else {
      swapCount++;
      swap(arr, i, arr.indexOf(arr, tempArr[i]));
    }
  }

  return swapCount;
};

arr = [5, 1, 3, 7, 9];
console.log(arrChallange(arr));
