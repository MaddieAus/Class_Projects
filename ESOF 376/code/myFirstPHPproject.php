<?php

	if (isset($_GET["Name"]) && isset($_GET["Place"])){
		$name = $_GET["Name"];
		$place = $_GET["Place"];
	echo "$name ! Welcome to ESOF 376 <br />";
	echo "Awesome! $place is a great place to visit.";
	}

?>