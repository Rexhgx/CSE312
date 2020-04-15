function get_new_post (post_id, post_text, post_photo_url){
    var new_post =  `
         <div class="share_box_post" id=${post_id.toString()}>
            <div class="share_box_post_user">
                    <img src="{% static "static/image/chat_and_share.png"%}" alt="User Photo" class="share_box_user_photo">
            </div>
            <div class="share_box_post_text">
                <h4 class="share_box_post_text_username"></h4>
                <p class="share_box_post_text_messages">${post_text}</p>
            </div>
          </div>
    `
    return new_post
}