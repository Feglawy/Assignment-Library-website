class Book {
  /*
  tittle : string
  description : string
  cover: string
  authors
  catagories: Array<string>
  type: string
  isAvailable: boolean = true
  */
  constructor(
    Tittle,
    Description,
    Cover,
    Authors,
    Catagories,
    Type,
    IsAvailable = true
  ) {
    this.tittle = Tittle;
    this.description = Description;
    this.cover = Cover;
    this.authors = Authors;
    this.catagories = Catagories;
    this.type = Type;
    this.isAvailable = IsAvailable;
  }
}

let bookMap = new Map();
let BorrowedBooksMap = new Map();

let tpn = new Book(
  "The Promised Neverland",
  "Emma, Norman and Ray are the brightest kids at the Grace Field House orphanage. And under the care of the woman they refer to as “Mom,” all the kids have enjoyed a comfortable life. Good food, clean clothes and the perfect environment to learn—what more could an orphan ask for? One day, though, Emma and Norman uncover the dark truth of the outside world they are forbidden from seeing.",
  "/Images/covers/TPN-cover-18.webp",
  ["Kaiu shirai"],
  ["action", "Horror", "mystery"],
  "manga",
  true
);
let jjk = new Book(
  "Jujutsu kaisen",
  "In a world where cursed spirits feed on unsuspecting humans, fragments of the legendary and feared demon Ryomen Sukuna have been lost and scattered about. Should any demon consume Sukuna’s body parts, the power they gain could destroy the world as we know it. Fortunately, there exists a mysterious school of jujutsu sorcerers who exist to protect the precarious existence of the living from the supernatural! Although Yuji Itadori looks like your average teenager, his immense physical strength is something to behold! Every sports club wants him to join, but Itadori would rather hang out with the school outcasts in the Occult Research Club. One day, the club manages to get their hands on a sealed cursed object. Little do they know the terror they’ll unleash when they break the seal…",
  "/Images/covers/jjk-cover.webp",
  ["Gege akutami"],
  ["action", "Horror", "Dark fantasy"],
  "manga",
  true
);
let TG = new Book(
  "Tokyo Ghoul",
  "Shy Ken Kaneki is thrilled to go on a date with the beautiful Rize. But it turns out that she's only interested in his body--eating it, that is. When a morally questionable rescue transforms him into the first half-human hal",
  "/Images/covers/TokyoGhoul-Vol-11.jpg",
  ["Sui Ishida"],
  ["action", "Supernatural thriller", "Dark fantasy"],
  "manga",
  true
);
let op = new Book(
  "One Piece",
  "As a child, Monkey D. Luffy dreamed of becoming King of the Pirates. But his life changed when he accidentally gained the power to stretch like rubber...at the cost of never being able to swim again! Years later, Luffy sets off in search of the One Piece, said to be the greatest treasure in the world...",
  "/Images/covers/one-piece-cover.jpg",
  ["Eiichiro Oda"],
  ["action", "comedy", "adventure", "super natural", "fantasy"],
  "manga",
  true
);
let soloLeveling = new Book(
  "Solo leveling",
  "After his victory on Jeju Island, the top guilds are all clamoring to recruit Jinwoo Sung, the strongest S-rank hunter and the hero of Korea―a far cry from the hapless E-rank hunter he used to be. As exciting as each new development is, however, Jinwoo’s eager to finally get some answers, so an invitation from the system to return to the double dungeon that changed his life is a welcome opportunity. He’ll have to put the visit on the back burner, though, because first things first―Jinwoo has a guild to establish!",
  "/Images/covers/solo-leveling-vol-3.jpg",
  ["Hye Young Im"],
  ["action", "comedy", "adventure", "super natural", "fantasy"],
  "manhwa",
  true
);
let aot = new Book(
  "Attack On Titan",
  "In this post-apocalyptic sci-fi story, humanity has been devastated by the bizarre, giant humanoids known as the Titans. Little is known about where they came from or why they are bent on consuming mankind. Seemingly unintelligent, they have roamed the world for years, killing everyone they see. For the past century, what's left of man has hidden in a giant, three-walled city. People believe their 50-meter-high walls will protect them from the Titans, but the sudden appearance of an immense Titan is about to change everything.",
  "/Images/covers/Aot-cover.jpg",
  ["Hajime Isayama"],
  ["Action ", "Dark fantasy", "Post-apocalyptic"],
  "manga",
  true
);
let moriarty = new Book(
  "Moriarty The Patriot",
  "The untold story of Sherlock Holmes’ greatest rival, Moriarty! <br> Before he was Sherlock’s rival, Moriarty fought against the unfair class caste system in London by making sure corrupt nobility got their comeuppance. But even the most well-intentioned plans can spin out of control—will Moriarty’s dream of a more just and equal world turn him into a hero…or a monster?",
  "/Images/covers/Moriarty-the-patriot.webp",
  ["Ryosuke Takeuchi"],
  ["Crime", "Mystery", "Thriller"],
  "manga",
  true
);
bookMap.set("TPN", tpn);
bookMap.set("JJK", jjk);
bookMap.set("TG", TG);
bookMap.set("OP", op);
bookMap.set("soloLeveling", soloLeveling);
bookMap.set("AOT", aot);
bookMap.set("moriarty", moriarty);

export { bookMap, BorrowedBooksMap };
