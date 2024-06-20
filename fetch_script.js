document.addEventListener('DOMContentLoaded', function () {
    fetch('/headlines')
        .then(response => response.json())
        .then(data => {
            const newsList = document.getElementById('news-list');
            data.forEach(article => {
                const listItem = document.createElement('li');
                const link = document.createElement('a');
                link.href = article.url;
                link.textContent = article.title;
                listItem.appendChild(link);
                newsList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching news:', error));
});
