# One Piece Wiki Search Microservice Backend

This document describes how to programmatically interact with the One Piece Wiki Search microservice backend.

## Requesting Data from the Microservice

To request data from this microservice, you need to send an HTTP GET request to the search endpoint. Your request must include the query parameter (`query`) to specify the search term.

### Example Request

Here's an example request using JavaScript's fetch API:

```javascript
fetch('http://localhost:8000/search?query=Luffy')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

Replace `Luffy` with any other keyword or phrase you wish to search for.

## Receiving Data from the Microservice

The microservice returns JSON-formatted responses structured as follows:

```json
{
  "query": "Luffy",
  "results": [
    {
      "page_number": 1,
      "headline": "Monkey D. Luffy",
      "description": "Captain of the Straw Hat Pirates aiming to become the Pirate King.",
      "tags": ["character", "pirates", "straw hats"],
      "relevance": 0.95
    }
  ]
}
```

- `query`: the original search query.
- `results`: an array containing matched pages, sorted by relevance. Each result includes:
  - `page_number`: identifier number of the page.
  - `headline`: title or main topic of the wiki page.
  - `description`: a brief description of the page content.
  - `tags`: relevant tags associated with the page.
  - `relevance`: a numerical score indicating how closely the page matches the search query.

### Example Code to Handle Received Data

Here is an example of how you might handle the received data:

```javascript
fetch('http://localhost:8000/search?query=Luffy')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(result => {
      console.log(`Page #${result.page_number}: ${result.headline}`);
      console.log(`Description: ${result.description}`);
      console.log(`Relevance: ${result.relevance}`);
    });
  })
  .catch(error => console.error('Error:', error));
```

You must implement your own logic to handle requests and responses. Do not rely on any provided test programs or existing client code.


