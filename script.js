fetch('data.json')
  .then(response => response.json())
  .then(data => {
    const tbody = document.querySelector('#allItems tbody');
    tbody.innerHTML = '';
    data.forEach(customer => {
      const row = `
        <tr>
          <td>${customer.Givenname} ${customer.Surname}</td>
          <td>${customer.Country}</td>
          <td>${customer.Birthday.split('-')[0]}</td>
        </tr>
      `;
      tbody.innerHTML += row;
    });
  })
  .catch(error => console.error('Error loading JSON:', error));
