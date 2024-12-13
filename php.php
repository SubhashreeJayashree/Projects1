<?php
// Enable CORS
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

// Get the input data
$data = json_decode(file_get_contents("php://input"), true);

if (isset($data['message'])) {
    $userMessage = strtolower(trim($data['message']));

    // Simple responses
    $responses = [
        "what courses do you offer?" => "We offer courses in Computer Science, Engineering, Business, and Arts.",
        "what is the admission process?" => "You can apply online through our portal or contact the admission office for assistance.",
        "what are the college timings?" => "The college operates from 8:00 AM to 5:00 PM, Monday to Friday.",
        "thank you" => "You're welcome! Feel free to ask more questions."
    ];

    // Generate response
    $reply = $responses[$userMessage] ?? "Sorry, I didn't understand that. Please try asking another question.";

    echo json_encode(["reply" => $reply]);
} else {
    echo json_encode(["reply" => "No input received."]);
}
?>