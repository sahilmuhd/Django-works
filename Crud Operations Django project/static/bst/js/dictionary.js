    const dictionary = {
      python: "A high-level programming language used for web, AI, and more.",
      javascript: "A scripting language used to create and control dynamic website content.",
      django: "A high-level Python Web framework that encourages rapid development.",
      html: "Standard markup language for creating web pages.",
      css: "A stylesheet language used for describing the look of a document."
    };

    function searchWord() {
      const word = document.getElementById("wordInput").value.toLowerCase().trim();
      const resultBox = document.getElementById("resultBox");

      if (dictionary[word]) {
        resultBox.innerHTML = `<strong>${word}:</strong> ${dictionary[word]}`;
      } else {
        resultBox.innerHTML = `Sorry, "${word}" is not in the dictionary.`;
      }
    }