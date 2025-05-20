fetch('data.json')
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById('list');
    data.forEach(profile => {
      const div = document.createElement('div');
      div.textContent = `${profile.name} - ${profile.email}`;
      list.appendChild(div);
    });
  });
