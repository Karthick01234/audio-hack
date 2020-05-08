<?php
session_start();
function start() {
    $a = 'audio';
    $b = $_POST['filename'];
    $c = $_FILES[$a]['tmp_name']; 
    $d = 'voice/' . $b;
    $e = pathinfo($d, PATHINFO_EXTENSION);
    if (!move_uploaded_file($c, $d)) {
        echo json_encode(array("statusCode"=>201)); 
    }
	else {
		echo json_encode(array("statusCode"=>200)); 
	}
}
start();
?>
