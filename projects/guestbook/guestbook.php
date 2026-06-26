<?php
/**
 * guestbook.php
 * -------------
 * A minimal guestbook endpoint.
 *
 *   GET  guestbook.php           -> returns all messages as JSON
 *   POST guestbook.php           -> adds a message ({ "name": ..., "message": ... })
 *
 * Messages are stored in messages.json next to this file. The goal of this
 * exercise is to show request handling, input validation, and avoiding a few
 * common mistakes (length limits, HTML escaping, no trust in user input).
 *
 * Note: PHP runs on a server, not on GitHub Pages. This file is included as a
 * code sample; to run it locally use:  php -S localhost:8000
 */

header("Content-Type: application/json");

const STORE = __DIR__ . "/messages.json";
const MAX_NAME = 40;
const MAX_MESSAGE = 280;

/** Load stored messages, or an empty list if the file is missing/corrupt. */
function load_messages(): array
{
    if (!file_exists(STORE)) {
        return [];
    }
    $data = json_decode(file_get_contents(STORE), true);
    return is_array($data) ? $data : [];
}

/** Save messages back to disk. */
function save_messages(array $messages): void
{
    file_put_contents(STORE, json_encode($messages, JSON_PRETTY_PRINT));
}

/** Send a JSON error and stop. */
function fail(int $code, string $reason): void
{
    http_response_code($code);
    echo json_encode(["error" => $reason]);
    exit;
}

$method = $_SERVER["REQUEST_METHOD"];

if ($method === "GET") {
    echo json_encode(load_messages());
    exit;
}

if ($method === "POST") {
    $input = json_decode(file_get_contents("php://input"), true);

    // Validate presence and type.
    if (!is_array($input) || empty($input["name"]) || empty($input["message"])) {
        fail(400, "Both 'name' and 'message' are required.");
    }

    $name = trim($input["name"]);
    $message = trim($input["message"]);

    // Validate length.
    if (strlen($name) > MAX_NAME) {
        fail(422, "Name is too long.");
    }
    if (strlen($message) > MAX_MESSAGE) {
        fail(422, "Message is too long.");
    }

    // Escape on the way in so stored data can be rendered safely.
    $entry = [
        "name"    => htmlspecialchars($name, ENT_QUOTES, "UTF-8"),
        "message" => htmlspecialchars($message, ENT_QUOTES, "UTF-8"),
        "at"      => date("c"),
    ];

    $messages = load_messages();
    $messages[] = $entry;
    save_messages($messages);

    http_response_code(201);
    echo json_encode($entry);
    exit;
}

fail(405, "Method not allowed.");
