import { Component, OnInit } from '@angular/core';
import { CrudService } from "../crud.service";
import { Globals } from "../Globals";

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {

  constructor(private backend: CrudService, public global: Globals) { }

  backGroundImage: string;

  ngOnInit(): void {
    this.backGroundImage = this.backend.PhotoUrl + "homepageBackground.jpg";
  }

}
