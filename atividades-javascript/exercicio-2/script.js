// Instruções do projeto
// Crie um projeto com dois arquivos: index.html e script.js. No arquivo 'index' insira a estrutura base HTML e dentro da tag 'body' inclua quatro tags vazias: h1, ul, a, ol. Adicione o atributo id="titulo" à tag h1, o atributo href="https://prozeducacao.com.br" à tag 'a', e o atributo id="lista-ordenada" à tag 'ol'. Na sequência, realize a conexão entre o arquivo HTML e o arquivo JavaScript.

// No arquivo script.js capture os quatro elementos criados, e use a propriedade .innerText para adicionar conteúdo textual aos elementos 'h1' e 'a', e a propriedade .innerHTML para adicionar três itens simples na lista não ordenada, e três itens com links para outros sites na lista ordenada.

const linksList = [
  "https://github.com/JOAO-LEE",
  "https://linkedin.com/in/joao-lee-lima",
  "https://x-clone-tan-seven.vercel.app/",
];

const title = document.querySelector("#titulo");
const prozLink = document.getElementsByTagName("a");
const unorderedList = document.getElementsByTagName("ul");
const orderedList = document.querySelector("#lista-ordenada");

title.innerText = "Proz Educação";

prozLink[0].innerText = "Clique aqui para saber mais!";

for (let index = 0; index < 3; index++) {
  unorderedList[0].innerHTML += `<li>Esse é o ite simples numero ${
    index + 1
  };</li>`;
}

orderedList.innerHTML = `<li><a href=${linksList[0]}>Meu GitHub!</a></li>
  <li><a href=${linksList[1]}>Meu LinkedIn</a></li>
  <li><a href=${linksList[2]}>Clone do X (antigo Twitter)</a></li>
  `;
