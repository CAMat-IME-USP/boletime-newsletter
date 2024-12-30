# Newsletter do BoletIME!

Script para facilitar a geração do corpo de e-mails para a newsletter do BoletIME.

## Como faço?

Para inserir as informações, edite o arquivo `info.yaml` inserindo as datas, novidades e posts desejados.

Com tudo pronto, rode o script principal

```shell
> py main.py
```

Um arquivo "output.html" será gerado. Agora basta enviá-lo como corpo de um e-mail!

## Sugestão para envio de e-mail

Uma forma de utilizar o arquivo gerado em um e-mail é via [Google Apps Script](https://script.google.com). Para isso, suba o arquivo HTML gerado para seu Google Drive, acesse o Google Apps Scripts com a mesma conta, crie um projeto de script e utilize o seguinte corpo de código (edite conforme desejado):

```gs
function enviarEmailComHTML() {
  var destinatario = "fulano@dominio.com";
  var assunto = "Assunto do e-mail";
  
  // Lê o arquivo HTML armazenado no Google Drive
  var arquivoHTML = DriveApp.getFileById("ID_DO_ARQUIVO_HTML");
  
  // Obtém o conteúdo HTML do arquivo
  var corpoHTML = arquivoHTML.getBlob().getDataAsString();  
  
  // Envia o e-mail com o corpo HTML
  MailApp.sendEmail({
    to: destinatario,
    subject: assunto,
    htmlBody: corpoHTML // Corpo do e-mail em HTML
  });
}
```

O `ID_DO_ARQUIVO_HTML` é o código que aparece na URL do arquivo no Google Drive. Por exemplo, para um arquivo em "https://drive.google.com/file/d/abobrinhadasilva/view", o ID é "abobrinhadasilva".