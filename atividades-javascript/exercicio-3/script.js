// Instruções do projeto
// Crie um projeto com dois arquivos: index.html e script.js. No arquivo 'index' insira apenas a estrutura base HTML e a tag script para conectar o arquivo HTML com o arquivo de extensão JavaScript.

// Usando os conceitos aprendidos nesse módulo, e sem alterar o arquivo index.html, adicione um título simples ao site com o id 'titulo', e um elemento que represente um produto à venda. O produto precisa incluir pelo menos o nome, a descrição e o preço. Pode incluir outros "elementos filhos" se achar necessário como, por exemplo, uma imagem. Procure usar o método simples e o método complexo, ensinados neste tópico.

const title = document.createElement("h1");
const elementForSell = document.createElement("div");
const productImage = document.createElement("img");
const productTitle = document.createElement("p");

title.innerText = "Items";
title.id = "titulo";

document.body.appendChild(title);
document.body.appendChild(elementForSell);
productImage.src = "https://imgnike-a.akamaihd.net/1300x1300/013923IDA8.jpg";
elementForSell.appendChild(productImage);
productTitle.innerText = "Tênis Nike Air Max 90 Feminino";
elementForSell.appendChild(productTitle);

elementForSell.innerHTML += `
<p>Nada é tão estiloso, confortável e aprovado: o Nike Air Max 90 permanece fiel às suas raízes com a icônica sola waffle, sobreposições costuradas e detalhes clássicos em TPU. Os detalhes novos oferecem um look moderno, enquanto o amortecimento Max Air adiciona conforto à sua jornada.</p>
<p>R$ 579,49 no Pix (R$ 999,99 42% off)
ou R$ 609,99 em até 6x sem juros (39% off)</p>`;
