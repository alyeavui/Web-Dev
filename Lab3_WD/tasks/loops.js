let i = 3;

while (i) {
  alert( i-- );
}

let j = 0;
while (++j < 5) alert( j );

let h = 0;
while (h++ < 5) alert( h );

for (let i = 0; i < 5; ++i) alert( i );

for (let i = 0; i < 5; i++) alert( i );

for (let i = 2; i <= 10; i++) {
    if (i % 2 == 0) {
      alert( i );
    }
  }

let m = 0;
while (m < 3) {
    alert( `number ${m}!` );
    m++;
}

let num;

do {
  num = prompt("Enter a number greater than 100?", 0);
} while (num <= 100 && num);


let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) { 

  for (let j = 2; j < i; j++) { 
    if (i % j == 0) continue nextPrime; 
  }

  alert( i ); 
}