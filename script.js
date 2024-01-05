$('#summarize-form').submit((e) => {
  e.preventDefault(); // Prevent the default form submission

  // Show loading indicator
  $('#result').removeClass('visually-hidden');
  $('#message').html('<div class="d-flex justify-content-center"><div class="spinner-border text-primary" role="status"></div></div>');

  // Get the article from the form
  let article = $('#article-input').val();

  // Encode the article text to safely include it in the URL
  //let encodedArticle = encodeURIComponent(article);

  // Send the article to the API
  axios({
    method: 'get',
    url: 'http://0.0.0.0:9000/',
    params: {
        text: article
    },
    headers: {
        'accept': 'application/json'
    }
}).then(
      (response) => {
          
          $('#result').addClass('alert-success');
          $('#message').html(response.data.pred);
      },
      (error) => {
          
          $('#result').addClass('alert-danger');
          $('#message').html(`An error occurred: ${error.message}`);
      },
  );
});
