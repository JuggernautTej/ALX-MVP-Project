const backendurl = 'https://tech-with-tej.pythonanywhere.com';

document.addEventListener('DOMContentLoaded', () => {
    loadHome();
});

function loadHome() {
    fetch(`${backendurl}/news/technology`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = createNewsGrid(data.news, 10);
        })
        .catch(error => console.error('Error fetching news:', error));
}

function loadTesla() {
    fetch(`${backendurl}/news/tesla`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = createNewsGrid(data.news, 10);
        })
        .catch(error => console.error('Error fetching news:', error));
}

function loadApple() {
    fetch(`${backendurl}/news/apple`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = createNewsGrid(data.news, 10);
        })
        .catch(error => console.error('Error fetching news;', error));
}

function loadAbout() {
    const content = document.getElementById('content');
    content.innerHTML = `
    <div class="about">
        <h2>About</h2>
        <p>Tech with Tej is a web service that provides the latest technology news, with focus on the most releavant headlines in the tech industry. Also, we provide the latest updates on Tesla and Apple.</p>
    </div>
    `;
}



function createNewsGrid(news, count) {
    const gridContainer = document.createElement('div');
    gridContainer.className = 'grid-container';
    news.slice(0, count). forEach(article => {
        const newsItem = document.createElement('div');
        newsItem.className = 'news-item';

        const imageUrl = article.urlToImage ? article.urlToImage : 'images/tech-news.jpg';
        const title = article.title ? article.title : 'Tech News';
        const author = article.author ? article.author : 'Friendly Neighborhood Tech Bro';
        const publishedAt = article.publishedAt ? new Date(article.publishedAt).toLocaleDateString() : '2024';
        const description = article.description ? article.description : 'Follow the "Read More" link and read the full article.';
        const articleUrl = article.url ? article.url : '#';

        newsItem.innerHTML = `
        <img src="${imageUrl}" alt="${title}">
        <h2>${title}</h2>
        <p>${description}</p>
        <p><small>By ${author} on ${publishedAt}</small></p>
        <a href="${articleUrl}" target="_blank">Read more</a>
        `;
        gridContainer.appendChild(newsItem);
    });
    return gridContainer.outerHTML;
}
