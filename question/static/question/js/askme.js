function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');


$('.like').on(
    'click', function () {
        el = $(this);

        qid = el.data('qid');
        vote = el.data('vote');
        data = {qid: qid, vote: vote};

        fetch(
            '/vote/', {
                method: 'POST',
                body: JSON.stringify(data),
                credentials: 'include',
                headers: {"X-CSRFToken": csrftoken},
            }
        )
            .then(response => response.json())
            .then(resp_data => {
                el.html(resp_data["resp"]);

            });
        return false;
    }
);


$('.dislike').on(
    'click', function () {
        el = $(this);

        qid = el.data('qid');
        vote = el.data('vote');
        data = {qid: qid, vote: vote};

        fetch(
            '/vote/', {
                method: 'POST',
                body: JSON.stringify(data),
                credentials: 'include',
                headers: {"X-CSRFToken": csrftoken},
            }
        )
            .then(response => response.json())
            .then(resp_data => {
                el.html(resp_data["resp"]);

            });
        return false;
    }
);