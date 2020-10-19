import { Injectable } from '@angular/core';
import { User } from './Interfaces';

@Injectable()
export class Globals  {
  public currentUser: User;
}