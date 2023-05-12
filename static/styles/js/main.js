$(document).ready(function() {
    console.log('Привет!');
    $.ajax({
        url: './answer.json"',
        dataType: 'json',
        success: function(data) {
            var events = data.map(function(event) {
                return {
                  title: event.title,
                  start: event.start,
                  end: event.end
                };
              });
            
              // Добавляем события в календарь
              $('#calendar').fullCalendar('addEventSource', events);
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.log(textStatus, errorThrown);
        }
      });
    
  });
