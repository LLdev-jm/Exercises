// Maps and Sets Exercise

// Quick Question #1
new Set([1,1,2,2,3,4]) 
{1,2,3,4}

//Quick Question #2
new Set([1,1,2,2,3,4]) 
'ref'

// Quick Questions #3
let m = new Map();
m.set([1,2,3], true);
m.set([1,2,3], false);

  0: {Array(3) => true}
  1: {Array(3) => false}

hasDuplicate
hasDuplicate([1,3,2,1]) // true
hasDuplicate([1,5,-1,4]) // false

function hasDuplicate(arr) {
  return new Set(arr).size !== arr.length;
}

//vowelCount
function vowelCount(string){
    const vowels = 'aeiou';
    const isVowel = (char) => vowels.indexOf(char.toLowerCase()) !== -1;
    const mappedString = new Map();

    for(let char of string.toLowerCase()) {
        if(isVowel(char)) {
            if(mappedString.has(char)) {
                mappedString.set(char, mappedString.get(char) + 1)
            } else{
                mappedString.set(char, 1)
            }
        }
    }
    return mappedString;
}