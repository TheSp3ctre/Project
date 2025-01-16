import fs from "fs/promises";

export default async function (error,file) {
    if (!file) {
        return `Por favor coloque o nome do arquivo.`;
    };
    await fs.writeFile('./logs/error.json',JSON.stringify({
        error,
        date: new Date().toDateString(),
        file: `Arquivo ${file}`
    }));
    return `Ocorreu um erro no código.Olhe o arquivo de erro na pasta logs.`;
};