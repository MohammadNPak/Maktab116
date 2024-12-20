console.log("this if from js");

function replyCallback(content_type, object_id) {
  console.log(
    `this is from button callback wiht ${content_type} and ${object_id}`
  );
}
