const products = [{
  image: 'image/athletic-cotton-socks-6-pairs.jpg',
  name: 'Black and Gray Athletic Cotton Socks - 6 pairs',
  rating: 'Something',
  priceinCents: 1090
},
{
  image: 'image/intermediate-composite-basketball.jpg',
  name: 'Intermediate Size Basketball',
  rating: 'Something',
  priceinCents: 2095
},
{
  image: 'image/adults-plain-cotton-tshirt-2-pack-teal.jpg' ,
  name:'Adults Plain Cotton T-Shirt - 2 Pack' ,
  rating: 'Something',
  priceinCents: 799
},
{
  image: 'image/black-2-slot-toaster.jpg' ,
  name:'2 Slot Toaster - Black' ,
  rating: 'Something',
  priceinCents: 1899
},
{
  image: 'image/6-piece-white-dinner-plate-set.jpg' ,
  name:'6 Piece White Dinner Plate Set' ,
  rating: 'Something',
  priceinCents: 2067
},
{
  image: 'image/6-piece-non-stick-baking-set.webp',
  name: '6-Piece Nonstick, Carbon Steel Oven',
  rating: 'Something',
  priceinCents: 3499
}];
/*Create an empty string to hold the value of html*/ 
let productsHTML = '';

products.forEach((product) => {
  productsHTML = productsHTML + `
      <div class="boxes">
        <div class="sock-row">
          <img src="${product.image}" class = "sock">
        </div>
        <div class="text-class">
          <div class="text-box">
            <p>${product.name}</p>
          </div>
          <p>${product.rating}</p>
          <p style="font-weight: bold;"> $${(product.priceinCents / 100).toFixed(2)} </p>
          <select id="numbers" name="numbers" class="select-button">
            <option value="1"> 1</option>
            <option value="2"> 2</option>
            <option value="3"> 3</option>
            <option value="4"> 4</option>
            <option value="5"> 5</option>
            <option value="6"> 6</option>
            <option value="7"> 7</option>
            <option value="8"> 8</option>
            <option value="9"> 9</option>
            <option value="10"> 10</option>
          </select>
        </div>
        <div class="add">
          <button class="add-Button">Add to Cart</button>
        </div>
      </div>  
  `;
});

document.querySelector('.js-struture').innerHTML = productsHTML;