const card1 = document.querySelector('.card1'),
      input1 = document.querySelector('.input1'),
      line2 = document.querySelector('.line2');
document.querySelector('.form1').addEventListener('submit', function(e) {
  input1.blur();
  card1.classList.add('saving');
  e.preventDefault();
});
line2.addEventListener('animationend', function(e) {
  setTimeout(() => {
    card1.classList.add('done');
  }, 1000);
});







