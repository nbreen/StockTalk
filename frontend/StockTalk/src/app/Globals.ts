import { Injectable } from '@angular/core';
//import { AnyNsRecord } from 'dns';
import { User } from './Interfaces';

@Injectable()
export class Globals  {
  public currentUser: User;
  public currentUsername: any;
}