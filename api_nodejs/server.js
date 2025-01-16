import express from "express";
import cors from "cors";
import axios from "axios";

import ValidatedParam from "./src/utils/validatedParam.js";
import writeLogs from "./src/utils/writeLogs.js";

const app = express();

app.use(cors());
app.use(express.json());

const PORT = 8080 || 8081;

app.post('/auth/register/user',async function (request,response) {
    const {username,password,confirmPassword} = request.body;
    const params = [
        {param:username,name:"nome de usuário"},{param:password,name: "senha"},{param:confirmPassword,name:"confirmação de senha"}
    ];
    for (const object of params) {
        const error = ValidatedParam(object.param,object.name);
        if (error) {
            return response.status(400).json({message: "Preencha o campo " + error + " corretamente."});
        };
    };
    if (password !== confirmPassword) {
        return response.status(400).json({message: "Suas senhas não se batem."});
    };
    try {
       const data = await axios.post('http://localhost:8000/auth/register/user',{
            username,
            password
       });
       return response.status(200).json(data);
    }
    catch (e) {
        const data = await writeLogs(e,'server.js');
        return response.status(500).json({message: "Erro no servidor,tente novamete mais tarde."});
    };
});

app.listen(PORT, () => {
    console.log(`Server Running ${PORT}`);
});