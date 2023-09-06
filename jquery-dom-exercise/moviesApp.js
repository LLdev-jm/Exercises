let moviesList = [];

function createMovieDataHTML(movie) {
    return `
        <tr>
            <td>${movie.title}</td>
            <td>${movie.rating}</td>
            <td><button class="remove-movie" data-movie-id="${movie.id}">Remove</button></td>
        </tr>
    `;
}

let titleSortOrder = 'asc';
let ratingSortOrder = 'asc';

function sortMoviesBy(property, order) {
    return moviesList.sort(function(a, b) {
        if (property === 'title') {
            const valueA = a[property].toUpperCase();
            const valueB = b[property].toUpperCase();
            if (order === 'asc') {
                return valueA.localeCompare(valueB);
            } else {
                return valueB.localeCompare(valueA);
            }
        } else if (property === 'rating') {
            const valueA = parseFloat(a[property]);
            const valueB = parseFloat(b[property]);
            if (order === 'asc') {
                return valueA - valueB;
            } else {
                return valueB - valueA;
            }
        }
    });
}

function updateMovieTable() {
    const sortedMovies = sortMoviesBy('title', titleSortOrder);

    $("#movie-table-body").empty();

    sortedMovies.forEach(function(movie) {
        const HTMLtoAppend = createMovieDataHTML(movie);
        $("#movie-table-body").append(HTMLtoAppend);


        $(`button[data-movie-id="${movie.id}"]`).on("click", function() {

            const index = moviesList.findIndex(item => item.id === movie.id);
            if (index !== -1) {
                moviesList.splice(index, 1);

                updateMovieTable();
            }
        });
    });
}


$(".fa-sort").on("click", function() {
    const property = $(this).data("property");
    if (property === "title") {
        titleSortOrder = titleSortOrder === "asc" ? "desc" : "asc";
    } else if (property === "rating") {
        ratingSortOrder = ratingSortOrder === "asc" ? "desc" : "asc";
    }
    updateMovieTable();
});

$('form').on('submit', function(event) {
    event.preventDefault();
    const titleValue = $('#title').val();
    const ratingValue = parseFloat($('#rating').val());

    if (titleValue.trim() !== '' && titleValue.length >= 2 && !isNaN(ratingValue) && ratingValue >= 0 && ratingValue <= 10) {
        const movieEntry = {
            id: moviesList.length,
            title: titleValue,
            rating: ratingValue,
        };

        moviesList.push(movieEntry);

        // Call the sorting function after adding a new movie
        updateMovieTable();

        $('#title').val('');
        $('#rating').val('');
    } else {
        if (titleValue.trim() === '' || titleValue.length < 2) {
            alert('Please enter a valid title with at least 2 characters.');
        } else {
            alert('Rating number has to be between 0 and 10');
        }
    }
});
