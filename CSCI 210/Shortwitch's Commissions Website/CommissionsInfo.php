<!DOCTYPE html>
<html lang="en-us">
    <body>
        <head>
        <meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <?php include 'Navbar.php';?>
<script>

</script>
            <title>Art Catalog</title>
            <link rel="stylesheet" href="StyleSheet/indexStyle.css">
        </head>
        <h6>Art Catalog</h6>
        <?php include 'searchbar.php';?>
        <p>here you will find my commission prices and examples of what that would look like</p>
        <!--this will have my commisions sheet and how to commission me-->
        <!--<div id="imgdiv2"><img src="..\img\CommsRef.jpg" width="700" height="600"></div> draw exsamples of what youll be selling, replace this-->
 <!--(grabs data),(carts->products), (customer->cart), (actual customer goes first)-->

 <!-- <select ProductID, imageID, Prodname, price, Quantity 
 left join cart ON products. ProductID = cart.products
 left join customers ON cart.custID =customers.custID WHERE custID = customer> -->

<div class="catalog">
  <div class="product-card">
    <img src="..\img\sketch2.png" width="350" height="400" alt="sketch2" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Bust Sketch</h2>
      <p class="product-description">This would be a sketch commission of the Bust up. Example shown above</p>
      <div class="product-price">$5.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\sketch1.png" width="350" height="400" alt="sketch1" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Torso Sketch</h2>
      <p class="product-description">This would be a sketch commission of the torso up. Example shown above</p>
      <div class="product-price">$6.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\sketch3.png" width="350" height="400" alt="sketch3" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Full Sketch</h2>
      <p class="product-description">This would be a sketch commission of the whole body. Example shown above</p>
      <div class="product-price">$10.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\line2.png" width="350" height="400" alt="line2" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Bust Line</h2>
      <p class="product-description">This would be a line commission of the Bust up. Example shown above</p>
      <div class="product-price">$12.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\line3.png" width="350" height="400" alt="line3" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Torso Line</h2>
      <p class="product-description">This would be a line commission of the torso up. Example shown above</p>
      <div class="product-price">$14.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\line1.png" width="350" height="400" alt="line1" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Full Line</h2>
      <p class="product-description">This would be a line commission of the whole body. Example shown above</p>
      <div class="product-price">$15.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>
</div>

<!--second catalog-->

<div class="catalog">
  <div class="product-card">
    <img src="..\img\flats2.png" width="350" height="400" alt="flats2" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Bust Flat</h2>
      <p class="product-description">This would be a flat commission of the Bust up. Example shown above</p>
      <div class="product-price">$17.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\flats3.png" width="350" height="400" alt="flats3" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Torso Flat</h2>
      <p class="product-description">This would be a flat commission of the torso up. Example shown above</p>
      <div class="product-price">$18.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\flats1.png" width="350" height="400" alt="flats1" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Full Flat</h2>
      <p class="product-description">This would be a flat commission of the whole body. Example shown above</p>
      <div class="product-price">$20.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\full2.png" width="350" height="400" alt="full2" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Bust Shaded</h2>
      <p class="product-description">This would be a Shaded commission of the bust up. Example shown above</p>
      <div class="product-price">$25.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\full3.png" width="350" height="400" alt="full3" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Torso Shaded</h2>
      <p class="product-description">This would be a Shaded commission of the torso up. Example shown above</p>
      <div class="product-price">$30.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>

  <div class="product-card">
    <img src="..\img\full1.png" width="350" height="400" alt="full1" class="product-image">
    <div class="product-info">
      <h2 class="product-title">Full Shaded</h2>
      <p class="product-description">This would be a Shaded commission of the whole body. Example shown above</p>
      <div class="product-price">$35.00</div>
      <button class="buy-button">Buy</button>
    </div>
  </div>
</div>


   <?php include 'footer.php';?>

    </body>
</html>