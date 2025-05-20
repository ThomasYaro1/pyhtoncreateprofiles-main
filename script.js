fetch('data.json')
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById('list');
    list.innerHTML = '';
    data.forEach(customer => {
      list.innerHTML += `<p>${customer.Givenname} ${customer.Surname} - ${customer.TelephoneCountryCode} ${customer.Telephone}</p>`;
    });
  });
