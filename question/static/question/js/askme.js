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
        this._callCount = this._callCount || 0; // static scoped variable
        if (this._callCount++ >= 1) {

            return;
        }
        el = $(this);

        qid = el.data('qid');
        vote = el.data('vote');
        type = el.data('type');
        console.log(el);
        data = {qid: qid, vote: vote, type: type};
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

        this._callCount = this._callCount || 0; // static scoped variable
        if (this._callCount++ >= 1) {

            return;
        }
        el = $(this);

        qid = el.data('qid');
        vote = el.data('vote');
        type = el.data('type');
        data = {qid: qid, vote: vote, type: type};
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


$('.checkbox').on(
    'click', function () {
        el = $(this);
        qid = el.data('qid');
        correct = el.data('correct');
        data = {qid: qid, correct: correct};
        fetch(
            '/checkbox/', {
                method: 'POST',
                body: JSON.stringify(data),
                credentials: 'include',
                headers: {"X-CSRFToken": csrftoken},
            }
        )
            .then(response => response.json())
            .then(resp_data => {
                el.checked = true;
                var kek = resp_data['resp'];
                el.html(kek.toString());
                console.log(kek);  // TODO нормально отображать чекбокс

            });
        return false;
    }
);




