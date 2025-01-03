
    const modal = document.getElementById('modal');
    const btn = document.getElementById('modalButton');
    const span = document.getElementsByClassName("close")[0];
    const submitModalButton = document.getElementById('submitModal');
    const freeText = document.getElementById('freeText');
    const modalForm = document.getElementById('modalForm');
    modalForm.addEventListener('submit', (event) => {
    event.preventDefault(); // フォームのデフォルトの送信動作を阻止
    const formData = new FormData(modalForm);
    // Ajaxでデータをサーバーに送信
    fetch('/debate_page', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // サーバーからのレスポンス処理
        console.log(data);
        // モーダルウィンドウを閉じる
    modal.style.display = "none";
    })
    .catch(error => {
        console.error('Error:', error);
    });
    });
    submitModalButton.onclick = function() {
  const text = freeText.value;
  // フォームにhiddenフィールドを追加して、JavaScriptで値を設定
  const hiddenInput = document.createElement('input');
  hiddenInput.type = 'hidden';
  hiddenInput.name = 'free_text';
  hiddenInput.value = text;
  document.querySelector('form').appendChild(hiddenInput);

  // フォームを送信
  document.querySelector('form').submit();
};

    btn.onclick = function() {
    modal.style.display = "block";
    }

    span.onclick = function() {
    modal.style.display = "none";
    }

    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }


    

  
