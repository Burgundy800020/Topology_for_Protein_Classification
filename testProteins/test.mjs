

import fs from "fs/promises"

fs.readFile("proteins.json")
    .then((res)=>JSON.parse(res))
    .then((res)=>{
        console.log(res.result_set.length)
    })