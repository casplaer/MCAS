const form = document.getElementById('login-form');
const username = document.getElementById('username');
const password = document.getElementById('password');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // отменяем действие по умолчанию (отправку формы)

  // отправляем запрос на сервер для проверки данных пользователя
  fetch('/login', {
    method: 'POST',
    body: JSON.stringify({ username: username.value, password: password.value }),
    headers: { 'Content-Type': 'application/json' }
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      // если данные пользователя верны, перенаправляем его на другую страницу
      window.location.href = '/dashboard';
    } else {
      // если данные пользователя неверны, выводим сообщение об ошибке
      alert(data.message);
    }
  })
  .catch(error => {
    // обрабатываем ошибку
    console.error(error);
  });
});
