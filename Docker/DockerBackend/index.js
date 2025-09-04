const express=require('express')

app=express()

const port=3000

app.get('/hi', (req,res)=>{
    res.send('Hello world')
})

app.listen(port, ()=>{
    console.log(`Listening on port ${port}`)
})