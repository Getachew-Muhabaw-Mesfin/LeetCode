/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
      const results = new Array(functions.length);
        let count = 0;
        functions.forEach((fn, i) => {
            fn()
            .then(val => {
                results[i] = val;
                count++;
                if(count === functions.length) resolve(results);
            })
            .catch(reason => reject(reason));
        });
    });

  
//   const promises = functions.map(fn => fn()); // Start all functions in parallel

//     const results = []; // Array to store resolved values

//     for (let i = 0; i < promises.length; i++) {
//         try {
//             const result = await promises[i]; // Await each promise's result
//             results[i] = result; // Store result in the same order
//         } catch (error) {
//             throw error; // Reject with the first error encountered
//         }
//     }

//     return results; // Return results if all promises resolve

}
/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */